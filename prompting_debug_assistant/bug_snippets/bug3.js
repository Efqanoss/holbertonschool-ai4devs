function findUserById(users, id) {
    console.log("Axtarış başlayır...");
    
    let foundUser = null;

    for (i = 0; i < users.length; i++) {
        let user = users[i];

        // Xəta 2: '==' yerinə '=' yazılıb (Mənimsətmə xətası)
        if (user.id = id) {
            foundUser = user;
        }
    }

    console.log("Tapılan istifadəçi: " + foundUser.name);
    
    return foundUser;
}

const userList = [{id: 1, name: "Ali"}, {id: 2, name: "Veli"}];
findUserById(userList, 3);
