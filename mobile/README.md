# OIC Listo – Flutter Mobile

Secure mobile client for listing Oracle OIC Gen3 Integrations.

## Notes

- Flutter SDK is **not** installed in this sandbox.
- Structure is ready. On your machine run:

```bash
cd mobile
flutter create . --project-name oic_listo
flutter pub get
flutter run
```

## Security focus

- `flutter_secure_storage` for credentials & tokens (iOS Keychain / Android Keystore)
- Never store secrets in SharedPreferences or plain files
