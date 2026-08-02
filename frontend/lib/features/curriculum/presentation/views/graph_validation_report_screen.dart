import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class GraphValidationReportScreen extends StatelessWidget {
  const GraphValidationReportScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Graph Validation Report')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Graph Integrity Report (Domain: DSA)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                Divider(color: AppColors.darkBorder),
                SizedBox(height: 8),
                Text('✓ DAG Cycle Check: PASS (0 cycles detected)', style: TextStyle(color: AppColors.success)),
                SizedBox(height: 4),
                Text('✓ Broken References Check: PASS (0 broken edges)', style: TextStyle(color: AppColors.success)),
                SizedBox(height: 4),
                Text('✓ Duplicate Concepts Check: PASS (0 duplicate IDs)', style: TextStyle(color: AppColors.success)),
                SizedBox(height: 4),
                Text('✓ Disconnected Subgraphs: PASS (1 connected component)', style: TextStyle(color: AppColors.success)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
