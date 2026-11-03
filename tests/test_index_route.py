import unittest
from unittest.mock import patch

import app


class IndexRouteTests(unittest.TestCase):
    def test_index_displays_monsters(self):
        monsters = [{'name': 'Vampiro', 'power': 'Volar'}]

        with patch.object(app.Monster, 'get_all', return_value=monsters) as get_all:
            response = app.app.test_client().get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Vampiro', response.data)
        self.assertIn(b'Volar', response.data)
        get_all.assert_called_once_with()

    def test_intentional_failure_for_deployment_gate(self):
        self.fail('Fallo intencional para verificar que el despliegue se bloquea')


if __name__ == '__main__':
    unittest.main()
