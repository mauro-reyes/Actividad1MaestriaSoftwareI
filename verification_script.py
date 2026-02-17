from builder.automovil_builder import AutomovilBuilderConcreto
from bridge.plataforma import Web, Movil
from bridge.notificacion import AlertaCritica, MensajeInformativo
from mediator.sala_chat import SalaChat
from mediator.usuario import Usuario

def test_builder():
    print("Testing Builder Pattern...")
    builder = AutomovilBuilderConcreto()
    builder.set_motor("V8") \
           .set_color("Rojo") \
           .set_llantas("R19") \
           .set_gps(True) \
           .set_techo(True)
    auto = builder.build()
    
    assert auto.motor == "V8"
    assert auto.color == "Rojo"
    assert auto.gps is True
    print("✅ Builder: Auto created correctly with properties accessible.")

def test_bridge():
    print("Testing Bridge Pattern...")
    # Test Web Platform + Critical Alert
    web_platform = Web()
    critica = AlertaCritica(web_platform)
    msg = critica.emitir("Error 500")
    assert "[Web]" in msg
    print("✅ Bridge: Web Critical Alert emitted correctly.")

    # Test Mobile Platform + Info Message
    movil_platform = Movil()
    info = MensajeInformativo(movil_platform)
    msg = info.emitir("Bienvenida")
    assert "[Móvil]" in msg
    print("✅ Bridge: Mobile Info Message emitted correctly.")

def test_mediator():
    print("Testing Mediator Pattern...")
    sala = SalaChat()
    
    u1 = Usuario("Ana", sala)
    u2 = Usuario("Beto", sala)
    
    assert "Ana" in sala.usuarios
    assert "Beto" in sala.usuarios
    
    u1.enviar("Hola a todos")
    
    historial = sala.historial
    assert len(historial) == 1
    assert "[Ana]: Hola a todos" in historial[0]
    print("✅ Mediator: Users registered and message sent correctly.")

if __name__ == "__main__":
    try:
        test_builder()
        test_bridge()
        test_mediator()
        print("\n🎉 ALL TESTS PASSED! The refactoring is solid.")
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
    except Exception as e:
        print(f"\n❌ EXCEPTION OCCURRED: {e}")
