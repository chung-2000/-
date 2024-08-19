git config use.name/.email 查看使用者名稱 email  
git config --global user.name "名稱"設定使用者名稱 name後面一定要有空格 
git config --global user.email "chung7113040006@gmail.com" 設定使用者email
untracked 未儲存
tracked 以追蹤
staged 以暫存
committed 以提交
新增git git init (但是需要進入到該檔案夾的終端機裡才能創建git )
cd 檔案夾名稱 進入到想進去的檔案夾
cd \ 回最原始的檔案夾
cd . 當前資料夾
cd..回上一層資料夾 
追蹤檔案 git add 檔案名稱 檔案名稱
git commit -m "更新的版本名稱" 將檔案作儲存
若修改檔案 ctrl + s 儲存後會出現M表示修改 M在按git add 作保存 
git add *.py 將所有副檔名為py的都加入至暫存區
git add . 將所有的檔案都丟到暫存區
拍照指令 git commit
修改
要存檔前要先確認資料夾路徑是否正確 否則會無法儲存5
git log --oneline 可以查詢修改備註與檔案
git diff 檔案編號 可以查詢先前檔案修改錢的差異
git checkout 檔案編號 可以回覆先前檔案
如果無法船上去 有可能是git 的master branch 不在最一開始的頭部
因此需要打git status  查看狀態 如果出現 紅字 代表頭部分支並未出現在最完整的狀態 
可以打git checkout master
他就會幫你修正為最新的是頭 
然後在檢查 git status  出現 On branch master
就可以上傳三步驟 
git remote add origin https://github.com/chung-2000/-.git
git branch -M main
git push -u origin main
如果後續修改其文件 
則是打 31 與32兩個指令及可
更新最主要指令 
ctrl + s                儲存
git add                 加入到暫存
git status              確認狀況
git cimmit -m""         存最新檔
git branch -M main      上傳第一步
git push -u origin main 上傳第二部
---
文件夾裡面不需要特別安裝git inig 
不然會無法上傳 
然後如若新增檔案 
直接git add 資料夾名稱 
再來就是上傳步驟 
---
