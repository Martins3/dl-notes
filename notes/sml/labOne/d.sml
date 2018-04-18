fun Mult' ([], a) = []
    | Mult' (r::R, a) = r * a :: (Mult' (R, a));

val data = [1, 2, 3, 4];
Mult'(data, 10);
