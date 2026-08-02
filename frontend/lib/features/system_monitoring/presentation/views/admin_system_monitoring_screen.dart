import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminSystemMonitoringScreen extends StatelessWidget {
  const AdminSystemMonitoringScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('System Health & Infrastructure Monitoring')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.monitor_heart_rounded, color: AppColors.success, size: 36),
              title: Text('API Status: OPERATIONAL (99.9%)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Database Latency: 4.2ms • Redis Cache: Healthy • Event Bus: Active', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
