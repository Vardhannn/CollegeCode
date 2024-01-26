while true
do
echo "**MENU****"
echo "
1. List of files.
2. Copying files.
3. Removing files.
4. Renaming files.
5. Linking files.
press [CTRL+C] TO EXIT"
echo "enter your choice "
read ch
case "$ch" in
1 ) echo "The list of file names."
ls -l || echo "These are file";;
2) echo "Enter the old filename."
read ofile
echo "Enter the new file name."
read nfile
cp $ofile $nfile && echo "Copied sucessfully." || echo "Copied is not possible." ;;
3 ) echo "Enter the file name to remove."
read rfile
rm -f $rfile && echo "Successfully removed." ;;
4 ) echo "Enter the old file name."
read ofile
echo "Enter the new file name."
read nfile
mv $ofile $nfile && echo "The file $ofile name renamed to $nfile." || echo "You
cann't Rename the file.".;;
5 ) echo "Enter the original filename."
read ofile
echo "Enter the new filename to link a file."
read lfile
ln $ofile $lfile && echo "Creat the linking file Sccessfully." || echo "You cann't
Linking the file.";; * )
echo "Invalid option."
Echo " Enter correct choice."
esac
done
