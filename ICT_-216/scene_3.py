import domoticz

def onDeviceChanged(device):
    # Vérifier si le nom de l'appareil et son état correspondent à la condition
    if device['name'] == '13_bouton 1' and device['status'] == 'Off':
        # Allumer l'appareil correspondant
        domoticz.device('lampe chambre 13').switchOn()

# Simuler un appareil qui change d'état (pour tester la fonction)
test_device = {
    'name': '13_bouton 1',
    'status': 'Off'
}

# Appeler la fonction avec le test_device
onDeviceChanged(test_device)
