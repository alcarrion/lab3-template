import unittest
import importlib.util
import subprocess

class PokemonTester(unittest.TestCase):
    """
        Pruebas para la clase POKEMON
    """
    
    def test_module_exist(self):
        """
        Prueba para verificar el módulo
        """
        try:
            spec = importlib.util.find_spec("pokemon")
            self.assertIsNotNone(spec, 
                "\n\n***********     ERROR: El módulo 'pokemon' no existe    *************\
                \n\n***********     Crea el archivo pokemon.py, con eso será suficiente")
        except ImportError:
            self.fail("\n\n***********  ERROR No se pudo cargar el módulo 'pokemon'     **************\n\n")

    def test_class_exists(self):
        """
        Probar la existencia de la clase
        """
        try:
            module = importlib.import_module("pokemon")
            self.assertTrue(hasattr(module, "Pokemon"),
                            "\n\n***********     La clase 'Pokemon' no existe en el módulo 'pokemon' *******\
                            \n***********     Asegúrate de crear la clase con el constructor\n")
        except ImportError:
            self.fail("No se pudo cargar el módulo 'pokemon'")

    def test_class_attributes(self):
        """
        Probar que exista el atributo
        """
        try:
            module = importlib.import_module("pokemon")
            Pokemon = getattr(module, "Pokemon")
            pokemon_instance = None
            try:
                pokemon_instance = Pokemon(id=1, name="Pikachu", weight=6.0, height=0.4, type="Electric", trainer="Ash")
            except Exception as e:
                self.fail(f"\n\n***********  No se pudo crear una instancia de Pokemon: ************\
                          \n***********  Asegúrate que existan los siguientes atributos:\
                          \n-'id' (entero)\
                          \n-'name' (cadena),\
                          \n- weight (flotante),\
                          \n- height(flotante)\
                          \n- type (cadena)\
                          \n- trainer (cadena)\
                          \n***********  No olvides que estos atributos también deben estar como parámetros del constructor ***********")

            self.assertIsInstance(pokemon_instance.name, str, "El atributo 'name' debe ser de tipo cadena de caracteres (str)")
            self.assertIsInstance(pokemon_instance.weight, float, "El atributo 'weight' debe ser de tipo flotante (float)")
            self.assertIsInstance(pokemon_instance.height, float, "El atributo 'height' debe ser de tipo flotante (float)")
            self.assertIsInstance(pokemon_instance.type, str, "El atributo 'type' debe ser de tipo cadena de caracteres (str)")
            self.assertIsInstance(pokemon_instance.trainer, str, "El atributo 'trainer' debe ser de tipo cadena de caracteres (str)")

            self.assertFalse(hasattr(pokemon_instance, "id"),
                            "\n\n***********  El atributo 'id' no debería ser accesible **************\
                            \nDebes renombrarlo como '__id' para que este sea privado")

            # Verificar que el método 'get_id' exista y devuelva un entero
            self.assertTrue(hasattr(pokemon_instance, "get_id"), "\n***********  El método 'get_id' no existe ***********")
            self.assertTrue(callable(getattr(pokemon_instance, "get_id")), "\n***********  El atributo 'get_id' debe ser un método ***********")
            self.assertIsInstance(pokemon_instance.get_id(), int, "\n***********  El método 'get_id' debe devolver un entero ***********")
            self.assertEqual(pokemon_instance.get_id(), 1, "\n*********** El método 'get_id' no devuelve el ID correcto ***********")

            # Verificar que el método 'set_id' solo acepte enteros
            self.assertTrue(hasattr(pokemon_instance, "set_id"), "\n***********  El método 'set_id' no existe ***********")
            self.assertTrue(callable(getattr(pokemon_instance, "set_id")), "\n***********  El atributo 'set_id' debe ser un método ***********")
            pokemon_instance.set_id(2)
            self.assertEqual(pokemon_instance.get_id(), 2, "\n*********** El método 'set_id' no cambia el ID correctamente ***********")
            with self.assertRaises(TypeError, msg="\n*********** El método 'set_id' debe lanzar un error TypeError si se le pasa un valor que no es un entero ***********"):
                pokemon_instance.set_id("Not an integer")

        except ImportError:
            self.fail("\n\n***********  No se pudo cargar el módulo 'pokemon' ***********")

    def test_str_method(self):
        """
        Prueba para verificar si la función __str__() está implementada en la clase Pokemon
        """
        try:
            module = importlib.import_module("pokemon")
            Pokemon = getattr(module, "Pokemon")
            pokemon_instance = None
            pokemon_instance = Pokemon(1, "Pikachu", 6.0, 0.4, "Electric", "Ash")
            expected_str = "Pikachu"
            self.assertEqual(str(pokemon_instance), expected_str,
                             "\n\n***********  El método __str__() debe estar creada dentro de la clase Pokemon y devolver el nombre del Pokemon ***********")
        
        except ImportError:
            self.fail("\n\n***********  No se pudo cargar el módulo 'pokemon' ***********")



class TrainerTester(unittest.TestCase):
    """
    Pruebas para la clase "Trainer"
    """
    
    def test_module_exists(self):
        """
        Verificar existencia de módulo
        """
        try:
            spec = importlib.util.find_spec("trainer")
            self.assertIsNotNone(spec, "\n\n*********** El módulo 'trainer' no existe   ***************\
                                 \nCrea el archivo trainer.py")
        except ImportError:
            self.fail("No se pudo cargar el módulo 'trainer'")

    def test_class_exist(self):
        """
        Prueba para verificar la existencia de la clase 'Trainer' dentro del módulo 'trainer'
        """
        try:
            module = importlib.import_module("trainer")
            self.assertTrue(hasattr(module, "Trainer"),
                            "\n\n***********     La clase 'Trainer' no existe en el módulo 'trainer' *******\
                            \n***********     Asegúrate de crear la clase con el constructor\n")
        except ImportError:
            self.fail("No se pudo cargar el módulo 'trainer'")

    def test_class_attributes(self):
        """
        Prueba para verificar que la clase 'Trainer' tenga los atributos requeridos
        """
        try:
            module = importlib.import_module("trainer")
            Trainer = getattr(module, "Trainer")
            trainer_instance = None
            try:
                trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
            except Exception as e:
                self.fail(f"\n\n***********  No se pudo crear una instancia de Trainer: ************\
                          \nAsegúrate de tener los siguientes atributos:\n\
                          \n- 'id' (entero)\
                          \n- 'first_name' (cadena),\
                          \n- 'last_name' (cadena),\
                          \n- 'age' (entero),\
                          \n- 'level' (entero)\
                          \n\nEstos atributos deben ser parámetros del constructor")

            self.assertIsInstance(trainer_instance.first_name, str, "El atributo 'first_name' debe ser de tipo cadena de caracteres (str)")
            self.assertIsInstance(trainer_instance.last_name, str, "El atributo 'last_name' debe ser de tipo cadena de caracteres (str)")
            self.assertIsInstance(trainer_instance.age, int, "El atributo 'age' debe ser de tipo entero")
            self.assertIsInstance(trainer_instance.level, int, "El atributo 'level' debe ser de tipo entero")

            # Verificar que el atributo 'id' sea privado
            self.assertFalse(hasattr(trainer_instance, "id"),
                            "\n\n***********  El atributo 'id' no debería ser accesible **************\
                            \nDebes renombrarlo como '__id' para que este sea privado")
            
            # Verificar que el método 'get_id' exista y devuelva un entero
            self.assertTrue(hasattr(trainer_instance, "get_id"), "\n***********  El método 'get_id' no existe ***********")
            self.assertTrue(callable(getattr(trainer_instance, "get_id")), "\n***********  El atributo 'get_id' debe ser un método ***********")
            self.assertIsInstance(trainer_instance.get_id(), int, "\n***********  El método 'get_id' debe devolver un entero ***********")
            self.assertEqual(trainer_instance.get_id(), 1, "\n*********** El método 'get_id' no devuelve el ID correcto ***********")

            # Verificar que el método 'set_id' exista y solo permita ingresar enteros
            self.assertTrue(hasattr(trainer_instance, "set_id"), "\n***********  El método 'set_id' no existe ***********")
            self.assertTrue(callable(getattr(trainer_instance, "set_id")), "\n***********  El atributo 'set_id' debe ser un método ***********")
            
            # Verificar que el método 'set_id' solo acepte enteros
            trainer_instance.set_id(2)
            self.assertEqual(trainer_instance.get_id(), 2, "\n*********** El método 'set_id' no cambia el ID correctamente ***********")
            with self.assertRaises(TypeError, msg="\n*********** El método 'set_id' debe lanzar un error TypeError si se le pasa un valor que no es un entero ***********"):
                trainer_instance.set_id("Not an integer")


        except ImportError:
            self.fail("\n\n***********  No se pudo cargar el módulo 'trainer'")

    def test_str_method(self):
        """
        Prueba para verificar si la función __str__() está implementada en la clase Trainer
        """
        try:
            module = importlib.import_module("trainer")
            Trainer = getattr(module, "Trainer")
            trainer_instance = None
            trainer_instance = Trainer(1, "Ash", "Ketchum", 10, 5)
            expected_str = "Ash Ketchum"
            self.assertEqual(str(trainer_instance), expected_str,
                "\n\n***********   El método __str__() debe estar creado en la clase Trainer y debe devolver el nombre y apellido del entrenador")
        except ImportError:
            self.fail("\n\n***********  No se pudo cargar el módulo 'trainer'")           
    

class TestMainModule(unittest.TestCase):
    """
        Clase para probar la clase principal
    """

    def test_module_exist(self):
        """
        Prueba para verificar la existencia del módulo principal
        """
        try:
            spec = importlib.util.find_spec("__main__")
            self.assertIsNotNone(spec, "\n\n***********     ERROR: El módulo principal no existe    *************")
        except ImportError:
            self.fail("\n\n***********  ERROR No se pudo cargar el módulo principal     **************\n\n")


if __name__ == '__main__':
    unittest.main()