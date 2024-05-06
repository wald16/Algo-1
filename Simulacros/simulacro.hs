
pertenece :: (Eq t) => [t] -> [t] -> Bool
pertenece [] a = True
pertenece (x:xs) a = elem x a && pertenece xs (quitar x a)


quitar :: (Eq t) => t -> [t] -> [t]
quitar x (y:ys) | x == y = ys
                | otherwise = y : quitar x ys

ambosIguales :: [(String, String)] -> Bool
ambosIguales [(x, y)] | x == y = True
                      | otherwise = False

personas' :: [(String, String)] -> [String]
personas' [] = []
personas' ((x, y):xs) =  x : y : personas' xs


noRep :: [String] -> [String]
noRep [] = []
noRep (x:xs) | pertenece [x] xs = noRep xs
             | otherwise = x : noRep xs

iterarPersonas :: [String] -> [(String, String)] -> [String]
iterarPersonas [] _ = []
iterarPersonas _ [] = []
iterarPersonas (persona:resto) lista = listaMasLarga (persona : amigosDe persona lista) (iterarPersonas resto lista)


listaMasLarga :: [String] -> [String] -> [String]
listaMasLarga lista1 lista2 | cardinal lista1 > cardinal lista2 = lista1
                            | otherwise = lista2

cardinal :: [a] -> Integer
cardinal [] = 0
cardinal (x:xs) = 1 + cardinal xs

------------------------------------------------------------------------------------------------------------------------------

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x, y):xs) | x == y = False
                              | pertenece [(y, x)] xs || pertenece [(x, y)] xs = False
                              | otherwise = relacionesValidas xs


personas :: [(String, String)] -> [String]
personas lista = noRep (personas' lista)


amigosDe :: String -> [(String, String)] -> [String]
amigosDe a [] = []
amigosDe a ((x, y):xs) | a == x = y : amigosDe a xs
                       | a == y = x : amigosDe a xs
                       | otherwise = amigosDe a xs


personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [] = []
personaConMasAmigos lista = head (iterarPersonas (personas lista) lista)



-- [("ana", "pedro"), ("ana", "martin"), ("jose", "matias"), ("matias", "chango"), ("juan", "matias")]                                              