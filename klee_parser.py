from klee import KTest

kt = KTest('klee-out-tiff-magic/test000001.ktest')
print(kt.objects[0].data)
