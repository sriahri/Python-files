coins = 64197
original_coins = coins
talent = 0
mina = 0
drachma = 0
talent = coins// 25200
coins = coins%25200
mina = coins//420
coins = coins%420
drachma = coins//6
coins = coins%6
print('Input\tTalents   Minae   Drachmae   oboloi')
print(original_coins,' \t  ',talent,'\t  ',mina,'\t   ',drachma,'\t     ',coins)