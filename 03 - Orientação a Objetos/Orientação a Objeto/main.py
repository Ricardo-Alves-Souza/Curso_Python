from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaNormal, AgenciaVirtual, AgenciaPremium


conta_ricardo = ContaCorrente('Ricardo Alves de Souza', '393.385.638-80', 2109,  15454)
conta_kelly = ContaCorrente('Kelly dos Santos Bezerra', '452.541.984-80', 2109, 15784)

cartao_ricardo = CartaoCredito('Ricardo A. Souza', 15454)
cartao_kelly = CartaoCredito('Kelly S. Bezerra', 15784)

agencia_virtual = AgenciaVirtual('www.site_agencia.com', 9845245876, 157874124586)
agencia_normal = AgenciaNormal(9785412587, 1578956212456)
agencia_premium = AgenciaPremium(9451478542, 96541123484512)
