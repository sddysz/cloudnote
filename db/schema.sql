drop table  if EXISTS users ;

create table users (
    id integer primary key autoincrement,
    email text,
    is_active Integer,
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

insert into users (email,pwd,username,is_active) values ('sddysz@126.com','111111','sddysz',1);

drop table  if EXISTS notebooks ;
create table notebooks (
    id integer primary key autoincrement,
    userId Integer,
    parentNotebookId Integer,
    seq Integer,
    title text,
    urlTitle text,
    numberNotes Integer,
    isTrash Integer,
    isBlog Integer,
    createdTime Integer,
    updatedTime Integer,
    usn Integer,
    isDeleted Integer
    
);

insert into notebooks (userId,title) values (1,'111111');
