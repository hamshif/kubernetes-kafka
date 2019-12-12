#!/usr/bin/env python
import os

from kafka_deploy import delete, get_ordered_cluster_res, get_ordered_zoo_res, get_ordered_kafka_res, ResType
from wield_services.wield.deploy.util import get_locale
from wielder.wrx.deployer import delete_pv, delete_pvc, delete_pvc_pv


def kafka_delete(del_cluster_assets=False, del_pv=True):

    namespace = 'kafka'
    locale = get_locale(__file__)

    print('break')

    module_root = locale.module_root.replace('/variants/', '')

    kafka_res = get_ordered_kafka_res()
    delete(res_tuples=kafka_res, module_root=module_root)

    zoo_res = get_ordered_zoo_res()
    delete(res_tuples=zoo_res, module_root=module_root)

    if del_pv:
        os.system(f'kubectl delete -f {module_root}/variants/docker-desktop/docker-storage.yaml --wait=false')
        print('tsav')
        delete_pvc_pv('data-kafka', namespace=namespace)
        print('mamoota')
        delete_pvc_pv('data-zoo', namespace=namespace)
        print('arnav')
        delete_pvc_pv('data-pzoo', namespace=namespace)

    if del_cluster_assets:

        res = get_ordered_cluster_res()

        for r in reversed(res):
            os.system(f'kubectl delete -f {module_root}/{r} --wait=false')


if __name__ == "__main__":

    print()
    kafka_delete()



