from app import create_app

app = create_app('development')

def test():
    """
    run the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run()
