import pytest
from quart.testing import QuartClient
from app import app, prepare_data
from datetime import datetime, timedelta

@pytest.fixture
def client():
    return QuartClient(app)

@pytest.mark.asyncio
async def test_main(client):
    response = await client.get('/')
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_search(client):
    response = await client.get('/search?q=test')
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_prepare_data(mocker):
    # Mock the db and the aggregate function
    db = mocker.MagicMock()
    db.aggregate.return_value.to_list.return_value = []

    # Call the function with the mocked db
    regions, region_colors, region_news, region_counts, top_words = await prepare_data(db, 6)

    # Assert the function calls and the returned values
    db.aggregate.assert_called_once()
    assert regions == []
    assert region_colors == {}
    assert region_news == {}
    assert region_counts == {}
    assert top_words == []