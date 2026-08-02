import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminBackupRestoreScreen extends StatelessWidget {
  const AdminBackupRestoreScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Enterprise Backup & System Restore')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.cloud_download_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Automated Daily Backup: HEALTHY', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Last Backup: Aug 2, 2026 • Size: 142.5 MB • Version Restore Available', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
