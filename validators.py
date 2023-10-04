def cpf(cpf):
    if len(cpf) == 11:
      first1 = int(cpf[0]) * 10
      first2 = int(cpf[1]) * 9
      first3 = int(cpf[2]) * 8
      first4 = int(cpf[3]) * 7
      first5 = int(cpf[4]) * 6
      first6 = int(cpf[5]) * 5
      first7 = int(cpf[6]) * 4
      first8 = int(cpf[7]) * 3
      first9 = int(cpf[8]) * 2

      seg_first1 = int(cpf[0]) * 11
      seg_first2 = int(cpf[1]) * 10
      seg_first3 = int(cpf[2]) * 9
      seg_first4 = int(cpf[3]) * 8
      seg_first5 = int(cpf[4]) * 7
      seg_first6 = int(cpf[5]) * 6
      seg_first7 = int(cpf[6]) * 5
      seg_first8 = int(cpf[7]) * 4
      seg_first9 = int(cpf[8]) * 3
      seg_first10 = int(cpf[9]) * 2

      total = (first1 + first2 + first3 + first4 + first5 + first6 + first7 + first8 + first9)
      division = (total // 11)
      left = (total - (11 * division))

      total_2 = (seg_first1 + seg_first2 + seg_first3 + seg_first4 + seg_first5 + seg_first6 + seg_first7 + seg_first8 + seg_first9 + seg_first10)
      division_2 = (total_2 // 11)
      left_2 = (total_2 - (11 * division_2))

      val_1 = False
      val_2 = False
      val_3 = False
      val_4 = False

      if(left <=1) and (cpf[9] == 0):
          val_1 = True
      if( left >=2 and left < 10) and (11 - left == cpf[9]):
          val_2 = True
      if( left_2 <=1 ) and (cpf[10] == 0):
          val_3 = True
      if ( left_2 >=2 and left_2 < 10 ) and (11 - left_2 == cpf[10]):
          val_4 = True
      else: ()

      if (val_1 == True or val_2 == True) and (val_3 == True or val_4 == True):
          print(f"O CPF número: {str(cpf)} é válido !")
      else:
          print(f"O CPF número: {str(cpf)} é inválido, tente novamente.")

      #Abaixo Validação dos estado de origem do CPF
      if cpf[8] == 1:
          print("Seu CPF é originário do estado do Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins")
      elif cpf[8] == 2:
          print("Seu CPF é originário do estado do Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima")
      elif cpf[8] == 3:
          print("Seu CPF é originário do estado do Ceará, Maranhão ou Piauí")
      elif cpf[8] == 4:
          print("Seu CPF é originário do estado de Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas")
      elif cpf[8] == 5:
          print("Seu CPF é originário do estado da Bahia; e Sergipe")
      elif cpf[8] == 6:
          print("Seu CPF é originário de Minas Gerais")
      elif cpf[8] == 7:
          print("Seu CPF é originário do estado do Rio de Janeiro ou Espírito Santo")
      elif cpf[8] == 8:
          print("Seu CPF é originário do estado de São Paulo")
      elif cpf[8] == 9:
          print("Seu CPF é originário do estado do Paraná ou Santa Catarina")
      else:
          print("Seu CPF é de origem do estado do Rio Grande do Sul")