# Generated by Django 3.0.3 on 2020-02-24 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkmatching', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultlink',
            old_name='autoexcusive',
            new_name='auto_exclu',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='down_from_node',
            new_name='down_from_no',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='traf_id_n',
            new_name='down_its_id',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='down_to_node',
            new_name='down_to_no',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='facility_kind',
            new_name='facil_kind',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='hov_buslane',
            new_name='hov_lane',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='lanes',
            new_name='lane',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='link_category',
            new_name='link_cate',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='maxspeed',
            new_name='max_spd',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='numcross',
            new_name='num_cross',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='road_facility_name',
            new_name='road_fac_na',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='shov_buslane',
            new_name='shov_lane',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='toll_name',
            new_name='tg_name',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='up_from_node',
            new_name='up_from_no',
        ),
        migrations.RenameField(
            model_name='resultlink',
            old_name='traf_id_p',
            new_name='up_its_id',
        ),
    ]
