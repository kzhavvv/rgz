import unittest
from app import app, db, Items  

class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        with app.app_context(): 
            db.create_all()

    def tearDown(self):
        with app.app_context(): 
            db.session.remove()
            db.drop_all()

    def test_add_item(self):
        response = self.app.post('/items', json={
            'name': 'Test Item',
            'quantity': 10,
            'price': 5.99,
            'category': 'Test Category'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Item added successfully', response.data)

    def test_get_items(self):
        with app.app_context():  
            item = Items(name='Test Item', quantity=10, price=5.99, category='Test Category')
            db.session.add(item)
            db.session.commit()

        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Item', response.data)

    def test_update_item(self):
        with app.app_context():
            item = Items(name='Test Item', quantity=10, price=5.99, category='Test Category')
            db.session.add(item)
            db.session.commit()
            item_id = item.id  

        # Теперь используем item_id
        response = self.app.put(f'/items/{item_id}', json={
            'quantity': 20
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Item updated successfully', response.data)

        with app.app_context():
            updated_item = Items.query.get(item_id)
            self.assertEqual(updated_item.quantity, 20)

    def test_delete_item(self):
        with app.app_context():
            item = Items(name='Test Item', quantity=10, price=5.99, category='Test Category')
            db.session.add(item)
            db.session.commit()
            item_id = item.id  

        # Теперь используем item_id
        response = self.app.delete(f'/items/{item_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Item deleted successfully', response.data)

        with app.app_context():
            deleted_item = Items.query.get(item_id)
            self.assertIsNone(deleted_item)


    def test_generate_report(self):
        with app.app_context():
            item1 = Items(name='Test Item 1', quantity=10, price=5.99, category='Category A')
            item2 = Items(name='Test Item 2', quantity=0, price=3.99, category='Category B')
            db.session.add_all([item1, item2])
            db.session.commit()

        response = self.app.get('/reports/summary')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Category A', response.data)
        self.assertIn(b'Category B', response.data)
        self.assertIn(b'Test Item 2', response.data)

if __name__ == '__main__':
    unittest.main()
