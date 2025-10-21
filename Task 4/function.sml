(* 5 function call examples that give an output. *)

fun f (x, y, z) = (x + y) * z;
print(f (1, 2, 4));

fun f (x: real, y: real, z: real) = (x + y) * z;
print (f (1.5, 2.5, 4.5));

fun f (x, y: real, z: real) = (x + y) * z;
print (f (1.5, 2.5, 4.5));

fun f (x, y, z: real): real = (x + y) * z;
print (f (1.5, 2.5, 4.5));

fun f (x, y, z): real = (x + y) * z;
print (f (1.5, 2.5, 4.5));

(* 5 function call examples that result in errors. *)

fun f (x, y, z) = (x + y) * z;
print(f (1.5, 2.5, 4.2));

fun f (x, y, z) = (x + y) * z;
print(f (1: real, 2, 4));

fun f (x: int, y: real, z) = (x + y) * z;
print(f (1.5, 2.5, 4.2));

fun f (x: int, y, z): real = (x + y) * z;
print(f (1.5, 2.5, 4.2));

fun f (x: int, y: int, z: real) = (x + y) * z;
print(f (1, 2, 4.2));

