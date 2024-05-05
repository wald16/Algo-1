--EJ1
-- a)
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- b) 
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

-- c)
todosMenosUlt :: [t] -> [t]
todosMenosUlt [x] = []
todosMenosUlt (x:xs) = x  : todosMenosUlt xs

-- d)
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]


--EJ2
-- 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) | x == y = True
                   | otherwise = pertenece x ys
-- 2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:xs) = x == ultimo (x:xs) && todosIguales (todosMenosUlt  (x:xs))

-- 3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) = not (pertenece x xs) && todosDistintos xs

-- 4) 
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

-- 5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == y = ys
                | otherwise = y : quitar x ys

-- 6) 
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys) | not (pertenece x (y:ys)) = (y:ys)
                     | x /= y = y : quitarTodos x ys
                     | otherwise = quitarTodos x ys

-- 7) 
eliminarRepetidos :: (Eq t) => [t] -> [t] 
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = x : quitarTodos x (eliminarRepetidos xs)
                         | otherwise = x : eliminarRepetidos xs

-- 8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] _ = True
mismosElementos (x:xs) ys = pertenece x ys && mismosElementos xs ys

-- 9) 
capicua :: (Eq t) => [t] -> Bool
capicua xs | xs == reverso xs = True
           | otherwise = False

