import unittest
from soa.service import SOAService
from soa.tiquets import GestioTiquets


class TestService(unittest.TestCase):

    def test_resultat_erroni_true(self):
        resultat = {'codiRetorn': "2"}
        self.assertTrue(SOAService.resultat_erroni(resultat))

    def test_resultat_erroni_false(self):
        resultat = {'codiRetorn': "1"}
        self.assertFalse(SOAService.resultat_erroni(resultat))

    def test_excepcio_retorna_resultat_erroni(self):        
        # El servei de gestio de tickets depen d'uns valors de settings que no son valids
        # Per tant la crida al servei farà saltar una excepció, que ens assegurarem
        # que ens transformi en un codiRetorn:-1
        tiquets=GestioTiquets()
        r=tiquets.alta_tiquet("jaume.moral", emailSolicitant='jaume.moral@upc.edu', client='', assumpte='PROVA', descripcio='PROVA', equipResolutor='106224', assignatA='', producte='UTIC-Z3.2', subservei='', urgencia='GRAVETAT_MITJA', impacte='', proces='PROCES_AUS', procesOrigen='', estat='TIQUET_STATUS_OBERT', ip='', enviarMissatgeCreacio='N', enviarMissatgeTancament='N', imputacioAutomatica='N', infraestructura='')
        self.assertTrue(SOAService.resultat_erroni(r))


if __name__ == '__main__':
    unittest.main()
