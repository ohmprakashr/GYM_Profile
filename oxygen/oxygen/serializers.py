from rest_framework import serializers
from .models import gymfield
class gymfieldserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=gymfield
		fields=('gymchoachname','datetime','Location','feesturcture')		