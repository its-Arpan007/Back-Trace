import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/shared/widgets/loading_indicator.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/splash/presentation/controllers/splash_controller.dart';

class SplashScreen extends ConsumerWidget {
  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final splashState = ref.watch(splashControllerProvider);

    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: AppColors.primaryGradient,
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 32.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                // Top Header Badge
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    StatusBadge(
                      label: splashState.isBackendConnected ? 'API Connected' : 'Connecting...',
                      isOnline: splashState.isBackendConnected,
                    ),
                    const Text(
                      'v1.0.0 (Foundation)',
                      style: TextStyle(
                        color: AppColors.textSecondaryDark,
                        fontSize: 12,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),

                // Center Branding & Diagnostic Engine Info
                Column(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(20),
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        gradient: AppColors.accentGradient,
                        boxShadow: [
                          BoxShadow(
                            color: AppColors.accentCyan.withOpacity(0.4),
                            blurRadius: 24,
                            spreadRadius: 4,
                          ),
                        ],
                      ),
                      child: const Icon(
                        Icons.psychology_outlined,
                        size: 64,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 24),
                    Text(
                      'BACKTRACE',
                      style: Theme.of(context).textTheme.displayLarge?.copyWith(
                            color: Colors.white,
                            letterSpacing: 4,
                            fontWeight: FontWeight.bold,
                          ),
                    ),
                    const SizedBox(height: 8),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
                      decoration: BoxDecoration(
                        color: AppColors.accentIndigo.withOpacity(0.2),
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(
                          color: AppColors.accentIndigo.withOpacity(0.5),
                        ),
                      ),
                      child: const Text(
                        'AI-POWERED LEARNING INTELLIGENCE PLATFORM',
                        style: TextStyle(
                          color: AppColors.accentCyan,
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 1.2,
                        ),
                      ),
                    ),
                    const SizedBox(height: 16),
                    Text(
                      'Diagnosing the root cause behind every answer.',
                      style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                            color: AppColors.textSecondaryDark,
                            fontStyle: FontStyle.italic,
                          ),
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),

                // Bottom Status Card
                AppCard(
                  child: Column(
                    children: [
                      if (splashState.isLoading)
                        const LoadingIndicator(
                          size: 32,
                        )
                      else
                        Icon(
                          splashState.isBackendConnected
                              ? Icons.check_circle_outline_rounded
                              : Icons.info_outline_rounded,
                          color: splashState.isBackendConnected
                              ? AppColors.success
                              : AppColors.warning,
                          size: 36,
                        ),
                      const SizedBox(height: 12),
                      Text(
                        splashState.statusMessage,
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                              color: AppColors.textPrimaryDark,
                              fontWeight: FontWeight.w500,
                            ),
                        textAlign: TextAlign.center,
                      ),
                      const SizedBox(height: 12),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          OutlinedButton(
                            onPressed: () {
                              ref.read(splashControllerProvider.notifier).checkSystemStatus();
                            },
                            style: OutlinedButton.styleFrom(
                              side: const BorderSide(color: AppColors.darkBorder),
                            ),
                            child: const Text(
                              'Test System',
                              style: TextStyle(color: AppColors.accentTeal),
                            ),
                          ),
                          const SizedBox(width: 12),
                          ElevatedButton.icon(
                            onPressed: () {
                              GoRouter.of(context).push('/ai-chat');
                            },
                            style: ElevatedButton.styleFrom(
                              backgroundColor: AppColors.accentTeal,
                            ),
                            icon: const Icon(Icons.auto_awesome_rounded, size: 18, color: Colors.white),
                            label: const Text(
                              'AI Study Assistant',
                              style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
