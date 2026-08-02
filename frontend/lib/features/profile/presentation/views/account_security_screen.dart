import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AccountSecurityScreen extends StatelessWidget {
  const AccountSecurityScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Account Security & Active Sessions')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: [
            AppCard(
              child: ListTile(
                leading: const Icon(Icons.devices_outlined, color: AppColors.accentTeal, size: 36),
                title: const Text('Flutter App Session (Current)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: const Text('Active • IP: 127.0.0.1', style: TextStyle(color: AppColors.textSecondaryDark)),
                trailing: const Icon(Icons.check_circle, color: AppColors.success),
              ),
            ),
            const SizedBox(height: 24),
            OutlinedButton.icon(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Revoked all other active sessions')),
                );
              },
              icon: const Icon(Icons.no_cell, color: AppColors.error),
              label: const Text('Revoke All Other Sessions', style: TextStyle(color: AppColors.error)),
            ),
          ],
        ),
      ),
    );
  }
}
