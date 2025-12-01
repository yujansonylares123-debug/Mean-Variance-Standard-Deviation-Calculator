import numpy as np

def calculate(numbers):
    # 1. Verificar que la lista contiene exactamente nueve números
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Convertir la lista en una matriz 3x3 de NumPy
    matrix = np.array(numbers).reshape(3, 3)

    # 3. Calcular las estadísticas requeridas
    mean_axis0 = np.mean(matrix, axis=0)
    mean_axis1 = np.mean(matrix, axis=1)
    mean_flat = np.mean(matrix)

    var_axis0 = np.var(matrix, axis=0)
    var_axis1 = np.var(matrix, axis=1)
    var_flat = np.var(matrix)

    std_axis0 = np.std(matrix, axis=0)
    std_axis1 = np.std(matrix, axis=1)
    std_flat = np.std(matrix)

    max_axis0 = np.max(matrix, axis=0)
    max_axis1 = np.max(matrix, axis=1)
    max_flat = np.max(matrix)

    min_axis0 = np.min(matrix, axis=0)
    min_axis1 = np.min(matrix, axis=1)
    min_flat = np.min(matrix)

    sum_axis0 = np.sum(matrix, axis=0)
    sum_axis1 = np.sum(matrix, axis=1)
    sum_flat = np.sum(matrix)

    # 4. Organizar los resultados en un diccionario
    calculations = {
        'mean': [
            mean_axis0.tolist(),          # Convertir a lista para JSON serializable
            mean_axis1.tolist(),          # Convertir a lista para JSON serializable
            mean_flat.item()              # Convertir a un escalar para JSON serializable
        ],
        'variance': [
            var_axis0.tolist(),
            var_axis1.tolist(),
            var_flat.item()
        ],
        'standard deviation': [
            std_axis0.tolist(),
            std_axis1.tolist(),
            std_flat.item()
        ],
        'max': [
            max_axis0.tolist(),
            max_axis1.tolist(),
            max_flat.item()
        ],
        'min': [
            min_axis0.tolist(),
            min_axis1.tolist(),
            min_flat.item()
        ],
        'sum': [
            sum_axis0.tolist(),
            sum_axis1.tolist(),
            sum_flat.item()
        ]
    }

    return calculations
