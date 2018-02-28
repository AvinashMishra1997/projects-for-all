def matmult(l , m):
    result=[[sum(a*b for a,b in zip(l_row,m_col)) for m_col in zip(*m)] for l_row in l]
    print(result)