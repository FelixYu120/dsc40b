def swap_sum(A, B):
    suma = sum(A)
    sumb = sum(B)
    need = (suma - sumb + 10) / 2

    i = 0
    j = 0
    a = len(A)
    b = len(B)
    while i < a & j < b:
        ai = A[i]
        bj = B[j]
        diff = ai - bj

        if diff == need:
            return (i, j)
        elif diff < need:
            i += 1
        else:
            j += 1

    return None
