
SOURCE_CODE1 = """
import java.util.ArrayList;
import java.util.List;

// This is a single-line comment
class HelloWorld {
    public static void main(String[] args) {
        /* This is a
           multi-line comment */
        boolean flag = true;
        String message = "Hello, World!";
        int number = 123;
        double pi = 3.14;
        int[] array = {1, 2, 3};
        if (flag == true) {
            System.out.println(message);
        }
        else {
            System.out.println("Flag is false.");
        }
    }
}

"""

SOURCE_CODE2 = """
// Definición de la clase del nodo del árbol
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

// Clase principal con la función de recorrido del árbol
class TreeTraversal {
    // Función de recorrido en profundidad primero (DFS)
    public static void DFS(TreeNode root) {
        if (root == null) {
            return;
        }

        // Imprimir el valor del nodo actual
        System.out.print(root.val + " ");

        // Recorrer el subárbol izquierdo
        DFS(root.left);

        // Recorrer el subárbol derecho
        DFS(root.right);
    }

    // Función principal para probar el recorrido del árbol
    public static void main(String[] args) {
        // Crear el árbol de ejemplo
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        // Realizar el recorrido en profundidad primero (DFS)
        System.out.println("Recorrido en profundidad primero (DFS):");
        DFS(root);
    }
}
"""

SOURCE_CODE3 = """
public class TrueFalseExample {
    public static void main(String[] args) {
        boolean isTrue = true;
        boolean isFalse = false;

        // Utilizando los valores booleanos en condiciones
        if (isTrue) {
            System.out.println("Esta condición es verdadera.");
        }

        if (!isFalse) {
            System.out.println("Esta condición es verdadera.");
        }

        // Utilizando los valores booleanos en operaciones booleanas
        boolean result1 = isTrue && isFalse;
        boolean result2 = isTrue || isFalse;
        boolean result3 = !isFalse;

        System.out.println("Resultado 1: " + result1);
        System.out.println("Resultado 2: " + result2);
        System.out.println("Resultado 3: " + result3);
    }
}
"""