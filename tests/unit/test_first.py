import pytest
from pyramid import testing

@pytest.fixture
def config():
    config = testing.setUp()
    yield config
    testing.tearDown()

@pytest.fixture
def testapp():
    from kordex0 import main
    from webtest import TestApp

    app = main({})
    yield TestApp(app)

def test_hello_world(config):
    from kordex0 import hello_world

    request = testing.DummyRequest()
    response = hello_world(request)
    assert response.status_code == 200

def test_hello_world_app(testapp):
    res = testapp.get('/', status=200)
    assert b'<h1>Hello World!</h1>' in res.body
