import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app.app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test if the index route returns 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_add_task(client):
    """Test adding a task"""
    response = client.post('/add_task',
                         data=json.dumps({'task': 'Test task'}),
                         content_type='application/json')
    assert response.status_code == 201
    assert response.json['status'] == 'success'

def test_get_tasks(client):
    """Test getting all tasks"""
    # First add a task
    client.post('/add_task',
                data=json.dumps({'task': 'Test task'}),
                content_type='application/json')
    
    # Then get all tasks
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert 'Test task' in response.json 