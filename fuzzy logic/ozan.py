
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as karar

#Giriş ve çıkışları tanımlıyoruz
gurultuseviyesi = karar.Antecedent(np.arange(30, 90, 1), 'gurultuseviyesi')
yas = karar.Antecedent(np.arange(0, 75, 1), 'yas')
sure = karar.Antecedent(np.arange(0, 9, 1), 'sure')
konforsuzluk = karar.Consequent(np.arange(0, 1, 0.01), 'konforsuzluk')

# Üyelik fonksiyonlarını sayıya göre otomatik oluşturma
"""
cekicilik.automf(5)
para.automf(3)
sure.automf(3)
konforsuzluk.automf(13)
"""

# Üyelik fonksiyonları türlerini tanımlama
gurultuseviyesi['Very Low'] = fuzz.trimf(gurultuseviyesi.universe, [30, 30, 45])
gurultuseviyesi['Low'] = fuzz.trimf(gurultuseviyesi.universe, [30, 45, 60])
gurultuseviyesi['Medium'] = fuzz.trimf(gurultuseviyesi.universe, [45, 60, 75])
gurultuseviyesi['High'] = fuzz.trimf(gurultuseviyesi.universe, [60, 75, 90])
gurultuseviyesi['Very High'] = fuzz.trimf(gurultuseviyesi.universe, [75, 90, 90])

yas['Young'] = fuzz.trimf(yas.universe, [0, 0, 35])
yas['Middle-Aged'] = fuzz.trimf(yas.universe, [30, 45, 60])
yas['Old'] = fuzz.trimf(yas.universe, [55, 75, 75])

sure['Short'] = fuzz.trimf(sure.universe, [0, 0, 5])
sure['Medium'] = fuzz.trimf(sure.universe, [4, 6, 7])
sure['Long'] = fuzz.trimf(sure.universe, [6, 9, 9])

konforsuzluk['extremely small'] = fuzz.trimf(konforsuzluk.universe, [0, 0.03, 0.06])
konforsuzluk['very very small'] = fuzz.trimf(konforsuzluk.universe, [0.05, 0.1, 0.15])
konforsuzluk['very small'] = fuzz.trimf(konforsuzluk.universe, [0.1, 0.2, 0.3])
konforsuzluk['small low'] = fuzz.trimf(konforsuzluk.universe, [0.22, 0.27, 0.32])
konforsuzluk['small'] = fuzz.trimf(konforsuzluk.universe, [0.3, 0.36, 0.42])
konforsuzluk['small high'] = fuzz.trimf(konforsuzluk.universe, [0.38, 0.42, 0.46])
konforsuzluk['medium low'] = fuzz.trimf(konforsuzluk.universe, [0.42, 0.48, 0.54])
konforsuzluk['medium'] = fuzz.trimf(konforsuzluk.universe, [0.5, 0.58, 0.66])
konforsuzluk['medium high'] = fuzz.trimf(konforsuzluk.universe, [0.62, 0.67, 0.72])
konforsuzluk['high'] = fuzz.trimf(konforsuzluk.universe, [0.68, 0.75, 0.82])
konforsuzluk['very high'] = fuzz.trimf(konforsuzluk.universe, [0.76, 0.83, 0.90])
konforsuzluk['very very high'] = fuzz.trimf(konforsuzluk.universe, [0.84, 0.91, 0.98])
konforsuzluk['extremely high'] = fuzz.trimf(konforsuzluk.universe, [0.96, 0.98, 1.0])


# Görüntüleme

gurultuseviyesi.view()
yas.view()
sure.view()
konforsuzluk.view()


kural1 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Young'] & sure['Short'], konforsuzluk['extremely small'])
kural2 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Young'] & sure['Medium'], konforsuzluk['very very small'])
kural3 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Young'] & sure['Long'], konforsuzluk['very small'])
kural4 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Middle-Aged'] & sure['Short'], konforsuzluk['very very small'])
kural5 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Middle-Aged'] & sure['Medium'], konforsuzluk['small'])
kural6 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Middle-Aged'] & sure['Long'], konforsuzluk['small high'])
kural7 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Old'] & sure['Short'], konforsuzluk['very very small'])
kural8 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Old'] & sure['Medium'], konforsuzluk['very small'])
kural9 = karar.Rule(gurultuseviyesi['Very Low'] & yas['Old'] & sure['Long'], konforsuzluk['small high'])
kural10 = karar.Rule(gurultuseviyesi['Low'] & yas['Young'] & sure['Short'], konforsuzluk['very small'])
kural11 = karar.Rule(gurultuseviyesi['Low'] & yas['Young'] & sure['Medium'], konforsuzluk['small low'])
kural12 = karar.Rule(gurultuseviyesi['Low'] & yas['Young'] & sure['Long'], konforsuzluk['small'])
kural13 = karar.Rule(gurultuseviyesi['Low'] & yas['Middle-Aged'] & sure['Short'], konforsuzluk['very small'])
kural14 = karar.Rule(gurultuseviyesi['Low'] & yas['Middle-Aged'] & sure['Medium'], konforsuzluk['medium low'])
kural15 = karar.Rule(gurultuseviyesi['Low'] & yas['Middle-Aged'] & sure['Long'], konforsuzluk['medium high'])
kural16 = karar.Rule(gurultuseviyesi['Low'] & yas['Old'] & sure['Short'], konforsuzluk['medium low'])
kural17 = karar.Rule(gurultuseviyesi['Low'] & yas['Old'] & sure['Medium'], konforsuzluk['medium'])
kural18 = karar.Rule(gurultuseviyesi['Low'] & yas['Old'] & sure['Long'], konforsuzluk['medium high'])
kural19 = karar.Rule(gurultuseviyesi['Medium'] & yas['Young'] & sure['Short'], konforsuzluk['very small'])
kural20 = karar.Rule(gurultuseviyesi['Medium'] & yas['Young'] & sure['Medium'], konforsuzluk['small'])
kural21 = karar.Rule(gurultuseviyesi['Medium'] & yas['Young'] & sure['Long'], konforsuzluk['medium low'])
kural22 = karar.Rule(gurultuseviyesi['Medium'] & yas['Middle-Aged'] & sure['Short'], konforsuzluk['medium'])
kural23 = karar.Rule(gurultuseviyesi['Medium'] & yas['Middle-Aged'] & sure['Medium'], konforsuzluk['high'])
kural24 = karar.Rule(gurultuseviyesi['Medium'] & yas['Middle-Aged'] & sure['Long'], konforsuzluk['very high'])
kural25 = karar.Rule(gurultuseviyesi['Medium'] & yas['Old'] & sure['Short'], konforsuzluk['medium high'])
kural26 = karar.Rule(gurultuseviyesi['Medium'] & yas['Old'] & sure['Medium'], konforsuzluk['very high'])
kural27 = karar.Rule(gurultuseviyesi['Medium'] & yas['Old'] & sure['Long'], konforsuzluk['very very high'])
kural28 = karar.Rule(gurultuseviyesi['High'] & yas['Young'] & sure['Short'], konforsuzluk['medium low'])
kural29 = karar.Rule(gurultuseviyesi['High'] & yas['Young'] & sure['Medium'], konforsuzluk['medium'])
kural30 = karar.Rule(gurultuseviyesi['High'] & yas['Young'] & sure['Long'], konforsuzluk['medium high'])



#kural1.view()
#kural2.view()
#kural3.view()

teklif_karar = karar.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8, kural9, kural10, kural11, kural12, kural13, kural14, kural15, kural16, kural17, kural18, kural19, kural20, kural21, kural22, kural23, kural24, kural25, kural26, kural27, kural28, kural29, kural30])

teklif_ = karar.ControlSystemSimulation(teklif_karar)

# Giriş değerleri...
teklif_.input['gurultuseviyesi'] = 35
teklif_.input['yas'] = 25
teklif_.input['sure'] = 3

# Hesap
teklif_.compute()

print(teklif_.output['konforsuzluk'])
konforsuzluk.view(sim=teklif_)
