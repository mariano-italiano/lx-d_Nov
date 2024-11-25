# Container startup process

1. Pobranie "base image" czyli wybranego obrazu (pod warunkiem że nie ma go na systemie hosta lokalnie).
2. Utworzenie kontenera.
3. Załadowanie systemu plików kontenera i utworzenie warstwy r/w (do odczytu i zapisu).
4. Inicjowanie połączenia sieciowego (sieć/interface typu bridge).
5. Konfiguracja sieci na kontenerze - interfejsu sieciowego.
6. Uruchomienie (zadania) kontenera.
7. Przechwycenie wyjścia - prowadzenie dziennika zdarzeń (logi).
