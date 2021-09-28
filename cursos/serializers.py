from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    
    # Nested Relationship (recomended mostly for one-to-one relationship)  
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field (mostly for one-to-many relationship)
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='avaliacao-detail'
    # )

    # Primary Key Related Field (ideal for milions of id's)
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'título',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
