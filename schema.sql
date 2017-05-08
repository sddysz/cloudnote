create table users (
     userId integer primary key autoincrement,
    email text,
    verified Integer,
    pwd  text,
    username  text,
    usernameRaw  text,
    createTime Integer,

    logo text,
    theme text,

    notebookWidth Integer,
    noteListWidth Integer,
    mdEditorWidth Integer,
    leftIsMin Integer,

    thirdUserId text,
    thirdUsername text,
    thirdType Integer,

    imageNum Integer,
    imageSize Integer,
    attachNum Integer,
    attachSize Integer,
    fromUserId text,

    accountType text,
    accountStartTime Integer,
    accountEndTime Integer,

    maxImageNum Integer,
    maxImageSize Integer,
    maxAttachNum Integer,
    maxAttachSize Integer,
    maxPerAttachSize Integer,

    usn Integer,
    fullSyncBefore Integer
);
