from skfuzzy import interp_membership as pertinencia

def fuzz_p(universo : list[int | float], mf : float, ipt: int | float):
    return pertinencia(universo,mf,ipt)
