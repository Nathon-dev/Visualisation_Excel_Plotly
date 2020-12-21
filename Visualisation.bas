Attribute VB_Name = "Visualisation_Plotly"
Sub Visualisation_Plotly()


' Adresse de l'outil
Adresse = "adequatePath"

Application.DisplayAlerts = False
Application.ScreenUpdating = False


    On Error Resume Next


Selection.Copy
    Workbooks.Add
    Selection.PasteSpecial Paste:=xlPasteValuesAndNumberFormats, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False




If Err.Number <> 0 Then
MsgBox "La sélection doit disposer du même nombre de lignes pour chaque colonne // The selection must have the same number of rows for each column"
    End If


   ActiveWorkbook.SaveAs Filename:= _
        Adresse & "\Data.csv", _
        FileFormat:=xlCSVUTF8, CreateBackup:=False


' In case UTF8 is not supported
    If Err.Number <> 0 Then
  ActiveWorkbook.SaveAs Filename:= _
        Adresse & "\Data.csv", _
        FileFormat:=xlCSV, CreateBackup:=False
      End If

ActiveWindow.Close

Application.DisplayAlerts = True
Application.ScreenUpdating = True


Call Shell(Adresse & "\visu.exe", vbHide)   'vbNormalFocus



End Sub
