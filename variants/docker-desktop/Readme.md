docker-desktop variant enables quick development on docker-desktop
=

Used simple bash scripts to deploy in order to simplify debugging 
first time the deployment is slow due to fetching images
Tested on mac

To init:     apply.sh 
To delete:   delete.sh`


To purge pvc after delete.sh
-
```
kubectl get all,pv,pvc -n kafka


kubectl patch persistentvolume/pvc-c6db42db-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch persistentvolume/pvc-c6dd08bc-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch persistentvolume/pvc-c6debfe3-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch persistentvolume/pvc-c66e4802-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch persistentvolume/pvc-c66fce03-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch persistentvolume/pvc-c671d115-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch persistentvolume/pvc-c6840151-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch persistentvolume/pvc-c68539e6-1205-11ea-bab6-025000000001 -p '{"metadata":{"finalizers": []}}' --type=merge
```

max.message.bytes