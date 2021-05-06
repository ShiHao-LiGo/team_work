# Generated by Django 2.2.13 on 2020-10-25 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20201010_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentannotation',
            name='relationship',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Relationship'),
        ),
        migrations.AddField(
            model_name='relationshipannotation',
            name='follow_sequenceAnnotation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow_sequenceAnnotation', to='api.SequenceAnnotation'),
        ),
        migrations.AddField(
            model_name='relationshipannotation',
            name='precursor_sequenceAnnotation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='precursor_sequenceAnnotation', to='api.SequenceAnnotation'),
        ),
        migrations.AddField(
            model_name='relationshipannotation',
            name='relationship',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Relationship'),
        ),
        migrations.AlterUniqueTogether(
            name='documentannotation',
            unique_together={('document', 'user', 'label', 'relationship')},
        ),
        migrations.AlterUniqueTogether(
            name='relationshipannotation',
            unique_together={('document', 'user', 'precursor_sequenceAnnotation', 'follow_sequenceAnnotation', 'relationship')},
        ),
        migrations.RemoveField(
            model_name='relationshipannotation',
            name='follow_label',
        ),
        migrations.RemoveField(
            model_name='relationshipannotation',
            name='follow_label_offset',
        ),
        migrations.RemoveField(
            model_name='relationshipannotation',
            name='precursor_label',
        ),
        migrations.RemoveField(
            model_name='relationshipannotation',
            name='precursor_label_offset',
        ),
    ]
