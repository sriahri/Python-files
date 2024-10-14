read -p "Enter username: " name
read -p "Enter Password: " Password
read -p "Enter Score: " Score

if [ $name = "jack" ] && [ $Password = "password" ];
then
if [ $Score -gt 30 ];
then
echo you got first place
elif [ $Score -gt 10 ];
then
echo you got second place
else
echo you got third place
fi
fi