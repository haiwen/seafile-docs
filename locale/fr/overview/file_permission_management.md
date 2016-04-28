# File permission management

Seafile gère les fichiers dans les bibliothèques. Chaque bibliothèque a un propriétaire, qui peut partager la bibliothèque à d'autres utilisateurs ou la partager avec des groupes. Le partage peut être en lecture seule ou en lecture-écriture.

## Synchronisation en lecture seule

Les bibliothèques en lecture seule peuvent être synchronisées localement. Les modifications sur le client local ne seront pas synchronisées. Si un utilisateurs a modifié le contenu d'un fichier, il/elle peut utiliser la "resynchronisation" pour annuler les modifications.


## Permissions héritées/permissions sur les sous-dossiers (édition Pro)

Le partage contrôle si un utilisateur/groupe peut voir une bibliothèque, tandis que les permissions sur les sous-dossiers sont utilisées pour les permissions de modifications sur ces dossiers uniquement. 

Supposons que vous partagez une bibliothèque en lecture seule à un groupe et que vous voulez ensuite que certains sous-dossiers soient en lecture-écriture pour quelques utilisateurs. Vous pouvez donner les permissions sur ces sous-dossiers aux utilisateurs et aux groupes ayant déjà accès au partage.

Note:

Donner les permissions sur un sous-dossier à un utilisateur sans avoir partagé le sous-dossier ou le dossier parent avec cet utilisateur n'aura aucun effet.
Partager une bibliothèque en lecture seule avec un utilisateur puis partager un sous-dossier en lecture-écriture avec cet utilisateur aura pour conséquence d'avoir deux éléments partagés avec cet utilisateur. Cela peut prêter à confusion. Utilisez plutôt les permissions sur les sous-dossiers.

