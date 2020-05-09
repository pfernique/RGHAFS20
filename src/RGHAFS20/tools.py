def SI(dataframe, unity, center=True):
    if not center:
        if unity == 'micro':
            return 10**(-6)*dataframe.X, 10**(-6)*dataframe.Y, 10**(-6)*dataframe.Z
        elif unity == 'mm':
            return 10**(-3)*dataframe.X, 10**(-3)*dataframe.Y, 10**(-3)*dataframe.Z
        elif unity == 'cm':
            return 10**(-2)*dataframe.X, 10**(-2)*dataframe.Y, 10**(-2)*dataframe.Z
        elif unity == 'dm':
            return 10**(-1)*dataframe.X, 10**(-1)*dataframe.Y, 10**(-1)*dataframe.Z
        elif unity == 'm':
            return dataframe.X, dataframe.Y, dataframe.Z
        else:
            raise ValueError('\'unity\' parameter')
    else:
        X, Y, Z = SI(dataframe, unity, False)
        return X-X.mean(), Y-Y.mean(), Z-Z.mean()
