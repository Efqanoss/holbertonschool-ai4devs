function findUserById(users, id) {
    console.log("Axtarış başlayır...");
    
    let foundUser = null;

    // Xəta 1: 'i' dəyişəni 'let' və ya 'var' ilə təyin edilməyib
    for (i = 0; i < users.length; i++) {
        let user = users[i];

        // Xəta 2: '==' yerinə '=' yazılıb (Mənimsətmə xətası)
        if (user.id = id) {
            foundUser = user;
            // Xəta 3: 'break' unudulub, dövr boş yerə davam edəcək
        }
    }

    // Xəta 4: 'undefined' obyektin xüsusiyyətinə müraciət xətası (null-check yoxdur)
    console.log("Tapılan istifadəçi: " + foundUser.name);
    
    return foundUser;
}

const userList = [{id: 1, name: "Ali"}, {id: 2, name: "Veli"}];
findUserById(userList, 3);
