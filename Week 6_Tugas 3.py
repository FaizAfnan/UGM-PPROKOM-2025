set_A = {20,30,40,50,60}
set_B = {25,30,35,40,45}
set_C = {30,40,50,70,80}
set_D = {40,50,60,90,100}

irisan_ABC = set_A & set_B & set_C
print(irisan_ABC)

Gabungan_AB = set_A | set_B
selisih_AB_D = Gabungan_AB - set_D 
print(selisih_AB_D)

selisih_simetris_BC = set_B ^ set_C
print(selisih_simetris_BC)

gabungan_AB= set_A | set_B
gabungan_CD = set_C | set_D
irisan_AB_CD = gabungan_AB & gabungan_CD
print(irisan_AB_CD)