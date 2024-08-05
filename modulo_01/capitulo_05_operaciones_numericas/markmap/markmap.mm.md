# Capítulo 5. Operaciones con datos numéricos y precedencia de operadores.

## Las operaciones básicas
- **Asignación** (`=`): Establece el valor de una variable.
- **Aritméticas**:
  - **Suma** (`+`): `a + b`
  - **Resta** (`-`): `a - b`
  - **Multiplicación** (`*`): `a * b`
  - **División** (`/`): `a / b`
  - **División entera** (`//`): `a // b`
  - **Módulo** (`%`): `a % b`
  - **Potenciación** (`**`): `a ** b`

## Precedencia de operadores
1. **Exponente** (`**`)
2. **Unarios** (`+x`, `-x`, `~x`)
3. **Multiplicación, División, División entera, Módulo** (`*`, `/`, `//`, `%`)
4. **Adición, Sustracción** (`+`, `-`)
- **Uso de paréntesis** (`()`): Modifica el orden de evaluación.

### Ejemplos de precedencia
- `2 + 3 * 4` ➜ `14`
- `(2 + 3) * 4` ➜ `20`
- `2 ** 3 * 4` ➜ `32`
- `10 / 2 + 3` ➜ `8.0`
- `10 // 3 + 2` ➜ `5`
- `10 % 3 + 2` ➜ `4`
- `-3 * 2 + 5` ➜ `-1`
- `2 + 3 * -4` ➜ `-10`

## El paquete math: Algunas funciones útiles
- **Raíz cuadrada**: `math.sqrt(25)` ➜ `5.0`
- **Valor absoluto**: `math.fabs(-10)` ➜ `10.0`
- **Funciones trigonométricas**:
  - `math.sin(math.pi / 4)`
  - `math.cos(math.pi / 4)`
  - `math.tan(math.pi / 4)`
- **Logaritmos**:
  - `math.log(10)`
  - `math.log10(100)`
- **Constantes matemáticas**:
  - `math.pi`
  - `math.e`

## Otros operadores
- **Comparación**:
  - `==` (igual)
  - `!=` (no igual)
  - `<` (menor que)
  - `>` (mayor que)
  - `<=` (menor o igual que)
  - `>=` (mayor o igual que)

### Ejemplos de comparación
- `5 == 10` ➜ `False`
- `5 != 10` ➜ `True`
- `5 < 10` ➜ `True`
- `5 > 10` ➜ `False`
- `5 <= 10` ➜ `True`
- `5 >= 10` ➜ `False`

- **Lógicos**:
  - `and` (y lógico)
  - `or` (o lógico)
  - `not` (negación)

### Ejemplos lógicos
- `True and False` ➜ `False`
- `True or False` ➜ `True`
- `not True` ➜ `False`

- **Identidad**:
  - `is` (es)
  - `is not` (no es)

### Ejemplos de identidad
- `[1, 2, 3] is [1, 2, 3]` ➜ `False`
- `[1, 2, 3] is not [1, 2, 3]` ➜ `True`
- `lista1 is lista3` ➜ `True`
