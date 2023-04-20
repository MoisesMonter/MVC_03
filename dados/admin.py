from django.contrib import admin
from django.db.models import Max
from .models import Eleicao,Dado_Eleicao

# Register your models here.
class EleicaoAdmin(admin.ModelAdmin):
    list_display =('eleicao_n','eleicao_nome','eleicao_ativo','Processo_do_Resultado')


    def Processo_do_Resultado(self,obj):
        data2 = Dado_Eleicao.objects.filter(eleicao_n = obj.eleicao_n).aggregate(Max('candidato_voto'))
        if len(data2) >1:
            return "Empate de votos"
        if data2['candidato_voto__max'] == 0:
            return "Sem votos"
        if data2['candidato_voto__max'] == None:
            return "Não há candidato"
        else:
            print(data2)
            result = Dado_Eleicao.objects.filter(candidato_voto =data2['candidato_voto__max'])
            print(result)
            if len(result)>1:
                return "Empatado"
            else:
                del(result)
                result = Dado_Eleicao.objects.get(candidato_voto =data2['candidato_voto__max'])
                return result.candidato_nome


class Dado_EleicaoAdmin(admin.ModelAdmin):
    list_display =('eleicao_n','candidato_nome','candidato_voto','test')

    def test (self,obj):
        filtered_position_to_string = str(obj.eleicao_n)
        data2 = Eleicao.objects.get(eleicao_n = int(filtered_position_to_string[-2:-1]))
        '''if data2.eleicao_ativo == True:
            return data2.eleicao_ativo
        else:
            return data2.eleicao_ativo'''
        return data2.eleicao_ativo
admin.site.register(Dado_Eleicao,Dado_EleicaoAdmin)
admin.site.register(Eleicao,EleicaoAdmin)



