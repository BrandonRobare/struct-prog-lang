// test_for_loop.t

print "Testing numeric array iteration:";
for (x in [1, 2, 3]) {
print x;
}

print "Testing empty array iteration:";
for (x in []) {
print x; // doesnt print anything
}

print "Testing iteration over object keys:";
obj = {"apple": 1, "banana": 2};
for (key in obj) {
print key;
}

print "Testing nested loops:";
for (x in [1, 2]) {
for (y in ["a", "b"]) {
print x;
print y;
}
}


print "All tests complete.";