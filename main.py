from customcrypt import CustomCrypt

mdp= "password"
customCrypt = CustomCrypt(mdp)
customCrypt.crypt()
print(f'Mdp chiffré : {customCrypt.mdp_chiffre}')